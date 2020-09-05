#include "bufferManagerMatrix.h"

class CursorMatrix
{
public:
    PageMatrix page;
    int pageIndex;
    string matrixName;
    int pagePointer;

    CursorMatrix(string matrixName, int pageIndex);
    vector<int> getNext();
    void nextPage(int pageIndex);
};