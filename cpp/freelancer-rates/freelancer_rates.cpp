// INFO: Headers from the standard library should be inserted at the top via
// #include <LIBRARY_NAME>
#include <cmath>
// daily_rate calculates the daily rate given an hourly rate
double daily_rate(double hourly_rate) {
    // TODO: Implement a function to calculate the daily rate given an hourly
    // rate
    double daily_billable_hours{8.0};
    return hourly_rate * daily_billable_hours;
}

// apply_discount calculates the price after a discount
double apply_discount(double before_discount, double discount) {
    // TODO: Implement a function to calculate the price after a discount.
    return before_discount * (1 - discount/100.0);
}

// monthly_rate calculates the monthly rate, given an hourly rate and a discount
// The returned monthly rate is rounded up to the nearest integer.
int monthly_rate(double hourly_rate, double discount) {
    // TODO: Implement a function to calculate the monthly rate, and apply a
    // discount.
    double monthly_billable_days = 22;
    double nominal_monthly_rate = 
        daily_rate(hourly_rate) * monthly_billable_days;
    return std::ceil(apply_discount(nominal_monthly_rate, discount));
}

// days_in_budget calculates the number of workdays given a budget, hourly rate,
// and discount The returned number of days is rounded down (take the floor) to
// the next integer.
int days_in_budget(int budget, double hourly_rate, double discount) {
    // TODO: Implement a function that takes a budget, an hourly rate, and a
    // discount, and calculates how many complete days of work that covers.
    // days = money / (money/hour) / (hour/day)
    // note to self - there are 8 billable hours per day haha, not 24
    double hourly_rate_discount = apply_discount(hourly_rate, discount);
    return std::floor(budget / daily_rate(hourly_rate_discount));
}
