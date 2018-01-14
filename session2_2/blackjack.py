from datetime import datetime
import itertools
# See here to understand the click library:
# http://click.pocoo.org/5/quickstart/#basic-concepts
import click


def random_number(x, c, m):
    ''' Produce a random number using the Park-Miller method.

    See http://www.firstpr.com.au/dsp/rand31/ for further details of this
    method. It is recommended to use the returned value as the value for x1,
    when next calling the method.'''
    return abs((c * x) % m)


def get_deck():
    '''Return a list of the all 52 playing cards.

    This list is sorted and always in the same order.
    '''
    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    rank = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    cards = list(itertools.product(rank, ['of'], suits))
    return [" ".join(l) for l in cards]


def get_random_card_from_deck(deck, x, c, m):
    ''' This element returns a random card from a given list of cards.

    Input:
      deck: list of available cards to return.
      x1: variable for use in the generation of random numbers.
      x2: variable for use in the generation of random numbers.
    '''
    x1 = random_number(x, c, m)
    card = deck.pop(x1 % len(deck))
    return (card, deck, x, c, m)


def blackjack_value(card):
    '''Return the value of a card when in the game of Blackjack.

    Input:
        card: A string which identifies the playing card.
    Strictly speaking, Aces can be valued at either 1 or 10, this
    implementation assumes that the value is always 1, and then determines
    later how many aces can be valued at 10.  (This occurs in
    blackjack_hand_value.)
    '''
    try:
        return int(card[:2])
    except ValueError:
        if card[:2] == 'Ac':
            return 1
        else:
            return 10


def is_ace(card):
    '''Identify whether or not a card is an ace.

    Input:
        card: A string which identifies the playing card.

    Returns:
        true or false, depending on whether the card is an ace or not.
    '''
    return card[:2] == 'Ac'


def blackjack_hand_value(cards):
    '''Calculate the maximal value of a given hand in Blackjack.

    Input:
        cards: A list of strings, with each string identifying a playing card.

    Returns:
        The highest possible value of this hand if it is a legal blackjack
        hand, or -1 if it is an illegal hand.
    '''
    sum_cards = sum([blackjack_value(card) for card in cards])
    num_aces = sum([is_ace(card) for card in cards])
    aces_to_use = max(int((21 - sum_cards) / 10.0), num_aces)
    final_value = sum_cards + 10 * aces_to_use
    if final_value > 21:
        return -1
    else:
        return final_value


def display(player, dealer):
    '''Display the current information available to the player.'''
    print('The dealer is showing : ' + dealer[0])
    print('Your hand is :' + repr(player))


def hit_me():
    '''Query the user as to whether they want another car or not.

    Returns:
        A boolean value of True or False.  True means that the user does want
        another card.
    '''
    ans = ""
    while ans.lower() not in ('y', 'n'):
        ans = input("Would you like another card? (y/n):")
    return ans.lower() == 'y'


@click.command()
@click.option(
    '--language',
    default='en',
    help='The language to play blackjack in, e.g. "en"')
def game(language):
    if language != 'en':
        raise ValueError("Language not recognized or implemented.")
    # Initialize everything

    x = int((datetime.utcnow() - datetime.min).total_seconds())
    # Constants given by the RANDU algorithm:
    # https://en.wikipedia.org/wiki/RANDU
    c = 65539
    m = 2147483648
    deck = get_deck()
    my_hand = []
    dealer_hand = []

    # Deal the initial cards
    for a in range(2):
        (card, deck, x, c, m) = get_random_card_from_deck(deck, x, c, m)
        my_hand.append(card)
        (card, deck, x, c, m) = get_random_card_from_deck(deck, x, c, m)
        dealer_hand.append(card)

    # Give the user as many cards as they want (without going bust).
    display(my_hand, dealer_hand)
    while hit_me():
        (card, deck, x, c, m) = get_random_card_from_deck(deck, x, c, m)
        my_hand.append(card)
        display(my_hand, dealer_hand)
        if blackjack_hand_value(my_hand) < 0:
            print("You have gone bust!")
            break

    # Now deal cards to the dealer:
    print("The dealer has : " + repr(dealer_hand))
    while 0 < blackjack_hand_value(dealer_hand) < 17:
        (card, deck, x, c, m) = get_random_card_from_deck(deck, x, c, m)
        dealer_hand.append(card)
        print("The dealer hits")
        print("The dealer has : " + repr(dealer_hand))

    if blackjack_hand_value(dealer_hand) < 0:
        print("The dealer has gone bust!")
    else:
        print('The dealer sticks with: ' + repr(dealer_hand))

    # Determine who has won the game:
    my_total = blackjack_hand_value(my_hand)
    dealer_total = blackjack_hand_value(dealer_hand)
    if dealer_total == my_total:
        print("It's a draw!")
    if dealer_total > my_total:
        print("The dealer won!")
    if dealer_total < my_total:
        print("You won!")


if __name__ == '__main__':
    game()
