#include "global.h"

CursorMatrix::CursorMatrix(string matrixName, int pageIndex)
{
    logger.log("CursorMatrix::CursorMatrix");
    this->page = bufferManagerMatrix.getPage(matrixName, pageIndex);
    this->pagePointer = 0;
    this->matrixName = matrixName;
    this->pageIndex = pageIndex;
}

/**
 * @brief This function reads the next row from the page. The index of the
 * current row read from the page is indicated by the pagePointer(points to row
 * in page the cursor is pointing to).
 *
 * @return vector<int> 
 */
vector<int> CursorMatrix::getNext()
{
    logger.log("CursorMatrix::geNext");
    vector<int> result = this->page.getValues();
    this->pagePointer++;
    if (result.empty())
    {
        matrixCatalogue.getMatrix(this->matrixName)->getNextPage(this);
        if (!this->pagePointer)
        {
            result = this->page.getValues();
            this->pagePointer++;
        }
    }
    return result;
}
/**
 * @brief Function that loads Page indicated by pageIndex. Now the cursor starts
 * reading from the new page.
 *
 * @param pageIndex 
 */
void CursorMatrix::nextPage(int pageIndex)
{
    logger.log("CursorMatrix::nextPage");
    this->page = bufferManagerMatrix.getPage(this->matrixName, pageIndex);
    this->pageIndex = pageIndex;
    this->pagePointer = 0;
}