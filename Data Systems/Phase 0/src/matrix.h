#include "cursorMatrix.h"

class Matrix
{
    vector<unordered_set<int>> distinctValuesInColumns;

public:
    string sourceFileName = "";
    string matrixName = "";
    vector<uint> distinctValuesPerColumnCount;
    long long columnCount = 0;
    uint pageCount = 0;
    uint blockCapacity = 0;
    bool indexed = false;
    string indexedColumn = "";
    IndexingStrategy indexingStrategy = NOTHING;

    bool extractColumnNumber();
    bool blockify();
    Matrix();
    Matrix(string matrixName);
    bool load();
    void print();
    void makePermanent();
    bool isPermanent();
    void getNextPage(CursorMatrix *cursor);
    CursorMatrix getCursor();
    void unload();
    void swap(int i,int j);
    int getElementAtPosition(int i, int j, bool first);
    void transpose();
    void writeElement(int val, int i, int j,bool fist);

    template <typename T>
    void writeRow(vector<T> row, ostream &fout)
    {
        logger.log("Table::printRow");
        for (int columnCounter = 0; columnCounter < row.size(); columnCounter++)
        {
            if (columnCounter != 0)
                fout << ", ";
            fout << row[columnCounter];
        }
        fout << endl;
    }

    template <typename T>
    void writeRow(vector<T> row)
    {
        logger.log("Table::printRow");
        ofstream fout(this->sourceFileName, ios::app);
        this->writeRow(row, fout);
        fout.close();
    }
};
