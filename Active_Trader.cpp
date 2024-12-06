#include "bits/stdc++.h"

// Function Declaration
std::vector<std::string> get_list(int n);
std::unordered_map<std::string, int> count_freq(std::vector<std::string> customers);
void print_customers_filtered(std::unordered_map<std::string, int> freq , float threshold);


// Main
int main(){
    int n;
    std::cin >> n;

    std::vector<std::string> customers(n) ;
    customers = get_list(n);
    
    std::sort(customers.begin(), customers.end(), std::greater<std::string>());

    auto customer_fr = count_freq(customers);       

    print_customers_filtered(customer_fr, (float)5*customers.size()/100);

    return 0;
}

// Function Definition
std::vector<std::string> get_list(int n) {
    std::vector<std::string> customers(n);
    for (int i = 0; i < n; i++){
        std::string str;
        std::cin >> str;
        customers[i] = str;
    }
    return customers;
}

std::unordered_map<std::string, int> count_freq(std::vector<std::string> customers){
    std::unordered_map<std::string, int> freq;
    for (int i = 0; i < customers.size(); i++){
        freq[customers[i]]++;
    }
    return freq;
}

void print_customers_filtered(std::unordered_map<std::string, int> freq , float threshold){
    for (auto& i : freq)
    {
        if (i.second >= threshold){
            std::cout << i.first << std::endl;
        }
    }
}
    