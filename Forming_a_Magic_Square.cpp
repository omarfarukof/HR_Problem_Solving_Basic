#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'formingMagicSquare' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY s as parameter.
 */

int formingMagicSquare(vector<vector<int>> s) {
    int d;
    vector<int> cost(8,0);
    vector<vector<int>> magic{{2,7,6},{9,5,1},{4,3,8}};

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            cost[0] += abs(s[i][j] - magic[i][j]);
            cost[1] += abs(s[i][j] - magic[j][i]);
            cost[2] += abs(s[i][j] - magic[j][2-i]);
            cost[3] += abs(s[i][j] - magic[2-i][j]);
            cost[4] += abs(s[i][j] - magic[2-i][2-j]);
            cost[5] += abs(s[i][j] - magic[2-j][2-i]);
            cost[6] += abs(s[i][j] - magic[2-j][i]);
            cost[7] += abs(s[i][j] - magic[i][2-j]);
        }
    }

    d = *min_element(cost.begin(), cost.end());

    return d;
}

int main()
{
    // ofstream fout(getenv("OUTPUT_PATH"));
    // ofstream fout("/dev/stdout");

    vector<vector<int>> s(3);

    for (int i = 0; i < 3; i++) {
        s[i].resize(3);

        string s_row_temp_temp;
        getline(cin, s_row_temp_temp);

        vector<string> s_row_temp = split(rtrim(s_row_temp_temp));

        for (int j = 0; j < 3; j++) {
            int s_row_item = stoi(s_row_temp[j]);

            s[i][j] = s_row_item;
        }
    }

    int result = formingMagicSquare(s);

    cout << result << "\n";

    // fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
