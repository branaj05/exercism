"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    # Solution 1: Prompt asks for a performant algorithm, 
    #   doing (//) every iteration seems unnecessary
    # seat_space = ['A', 'B', 'C', 'D']
    # n_vals_in_space = len(seat_space)
    # for n in range(number):
    #     row_number_index0 = (n // n_vals_in_space)
    #     remainder = n - row_number_index0 * n_vals_in_space
    #     yield seat_space[remainder]

    # Solution 2 - Accidentialy defeated the whole point of a generator 
    #   - pre-computing the entire space and then unpacking them one at a time
    # seat_space = ['A', 'B', 'C', 'D']
    # n_vals_in_space = len(seat_space)
    # n_min_rows = number//n_vals_in_space
    # remainder = number - n_min_rows * n_vals_in_space
    # seat_space = seat_space * n_min_rows + seat_space[:]
    # for seat in seat_space:
    #     yield seat

    # Solution 3 - Simple
    seat_space = ['A', 'B', 'C', 'D']
    remainder = -1
    for _ in range(number):
        if remainder == 3:
            remainder = -1
        remainder += 1
        yield seat_space[remainder]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    # Solution 1
    seat_space = ['A', 'B', 'C', 'D']
    n_vals_in_space = len(seat_space)
    # exception logic for unlucky row number 13
    if number // n_vals_in_space >= 13:
        number += n_vals_in_space

    for n in range(number):
        row_number_index0 = (n // n_vals_in_space) # There is likely a more performant solution than doing this // operation every loop
        if row_number_index0 == 12:
            # if on row 13 (12 if 0 indexed) skip and don't hit the yield
            continue
        remainder = n - row_number_index0 * n_vals_in_space
        # print(row_number_index0)
        yield f'{row_number_index0+1}{seat_space[remainder]}'



def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    return {name: val for name, val in zip(passengers, generate_seats(len(passengers)))}


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        base_len = len(seat) + len(flight_id)
        n_zeros = 12-base_len
        yield f"{seat}{flight_id}{'0'*n_zeros}"
