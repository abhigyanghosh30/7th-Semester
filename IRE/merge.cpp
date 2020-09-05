#include <bits/stdc++.h>
using namespace std;
int main()
{
    for (int i = 1; i <= 3; i += 2)
    {
        char filename1[100];
        char filename2[100];
        char outfilename[100];
        sprintf(filename1, "ind%d.txt", i);
        sprintf(filename2, "ind%d.txt", i + 1);
        sprintf(outfilename, "ind%d%d.txt", i, i + 1);
        ifstream infile1(filename1);
        ifstream infile2(filename2);
        ofstream outfile(outfilename);
        string line1, line2;
        string word1, word2;
        getline(infile1, line1);
        getline(infile2, line2);
        stringstream ss1(line1), ss2(line2);
        getline(ss1, word1, ':');
        getline(ss2, word2, ':');
        while (true)
        {
            cout << word1 << " " << word2 << endl;
            // stringstream ss1(line1), ss2(line2);
            if (word1.compare(word2))
            {
                outfile << line1 << endl;
                if (!getline(infile1, line1))
                {
                    break;
                }
                stringstream ss1(line1);
                getline(ss1, word1, ':');
            }
            else
            {
                outfile << line2 << endl;
                if (!getline(infile2, line2))
                {
                    break;
                }
                stringstream ss2(line2);
                getline(ss2, word1, ':');
            }
        }
    }
}