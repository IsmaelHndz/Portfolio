def nth_lowest_selling(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """

    sales_count = {}
    for book_id in sales:
        if book_id in sales_count:
            sales_count[book_id] += 1
        else:
            sales_count[book_id] = 1
    sorted_sales_count = sorted(sales_count.items(), key=lambda x: x[1])

    return sorted_sales_count [n-1] [0]

if __name__ == "__main__":
    print(nth_lowest_selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))