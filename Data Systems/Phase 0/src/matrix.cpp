#include "global.h"

Matrix::Matrix()
{
    logger.log("Matrix::Matrix");
}

Matrix::Matrix(string matrixName)
{
    logger.log("Matrix::Matrix");
    this->sourceFileName = "../data/" + matrixName + ".csv";
    this->matrixName = matrixName;
}
bool Matrix::load()
{
    logger.log("Matrix::load");
    fstream fin(this->sourceFileName, ios::in);
    string line;
    if (getline(fin, line))
    {
        fin.close();
        if (this->extractColumnNumber())
            if (this->blockify())
                return true;
    }
    fin.close();
    return false;
}

bool Matrix::extractColumnNumber()
{
    logger.log("Matrix::extractColumnNuber");
    fstream fin(this->sourceFileName, ios::in);
    string firstLine;
    getline(fin, firstLine);
    stringstream s(firstLine);
    string word;
    uint count = 0;
    while (getline(s, word, ','))
    {
        count++;
    }
    this->columnCount = count;
    this->blockCapacity = (uint)((BLOCK_SIZE * 1024) / sizeof(int));
    return true;
}

bool Matrix::blockify()
{
    logger.log("Matrix::blockify");
    ifstream fin(this->sourceFileName, ios::in);
    string line, word;
    vector<int> pageData;
    int sizeCounter = 0;
    while (getline(fin, line))
    {
        stringstream s(line);
        while (getline(s, word, ','))
        {
            pageData.push_back(stoi(word));
            sizeCounter++;
            if (sizeCounter == this->blockCapacity)
            {
                bufferManagerMatrix.writePage(this->matrixName, this->pageCount, pageData, blockCapacity);
                this->pageCount++;
                sizeCounter = 0;
                pageData.clear();
            }
        }
    }
    if (sizeCounter)
    {
        bufferManagerMatrix.writePage(this->matrixName, this->pageCount, pageData, blockCapacity);
        this->pageCount++;
    }
    return true;
}

void Matrix::getNextPage(CursorMatrix *cursor)
{
    logger.log("Matrix::getNext");

    if (cursor->pageIndex < this->pageCount - 1)
    {
        cursor->nextPage(cursor->pageIndex + 1);
    }
}

void Matrix::makePermanent()
{
    logger.log("Matrix::makePermanent");
    if (!this->isPermanent())
        bufferManagerMatrix.deleteFile(this->sourceFileName);
    string newSourceFile = "../data/" + this->matrixName + ".csv";
    ofstream fout(newSourceFile, ios::out);

    // CursorMatrix cursor(this->matrixName, 0);
    int currentPage = 0;
    vector<int> row;
    PageMatrix page = bufferManagerMatrix.getPage(this->matrixName, currentPage);
    vector<int> values = page.getValues();
    int sizeCount = 0;
    while (true)
    {
        for (vector<int>::iterator it = values.begin(); it != values.end(); it++)
        {
            row.push_back(*it);
            sizeCount++;
            if (sizeCount == this->columnCount)
            {
                this->writeRow(row, fout);
                sizeCount = 0;
                row.clear();
            }
        }
        currentPage++;
        if (currentPage == this->pageCount)
            break;
        page = bufferManagerMatrix.getPage(this->matrixName, currentPage);
        values = page.getValues();
    }
    fout.close();

    return;
}

bool Matrix::isPermanent()
{
    logger.log("Matrix::isPermanent");
    if (this->sourceFileName == "../data/" + this->matrixName + ".csv")
        return true;
    return false;
}

void Matrix::unload()
{
    logger.log("Matrix::~unload");
    for (int pageCounter = 0; pageCounter < this->pageCount; pageCounter++)
        bufferManager.deleteFile(this->matrixName, pageCounter);
    if (!isPermanent())
        bufferManager.deleteFile(this->sourceFileName);
}

CursorMatrix Matrix::getCursor()
{
    logger.log("Matrix::getCursor");
    CursorMatrix cursor(this->matrixName, 0);
    return cursor;
}

int Matrix::getElementAtPosition(int i, int j, bool first)
{
    logger.log("Matrix::Get element");

    long long int elementsToSee = i * this->columnCount + j;
    long long int elementsSeen = 0;
    int pageNumber = elementsToSee / this->blockCapacity;
    PageMatrix page;
    vector<int> values;
    if (first)
    {
        if (pageNumber != firstPageNumber)
        {
            firstPage = PageMatrix(this->matrixName, pageNumber);
            firstPageNumber = pageNumber;
        }
        values = firstPage.getValues();
    }
    else
    {
        page = PageMatrix(this->matrixName, pageNumber);
        values = page.getValues();
    }
    int elementInVector = elementsToSee % this->blockCapacity;
    return values[elementInVector];
}

void Matrix::writeElement(int element, int i, int j, bool first)
{

    logger.log("Matrix:: Write element");
    long long int elementsToSee = i * this->columnCount + j;
    long long int elementsSeen = 0;
    int pageNumber = elementsToSee / this->blockCapacity;
    PageMatrix page;
    page = PageMatrix(this->matrixName, pageNumber);
    vector<int> values;
    values = page.getValues();
    int elementInVector = elementsToSee % this->blockCapacity;
    values[elementInVector] = element;

    page.setValues(values);
    page.writePage();
}
void Matrix::swap(int i, int j)
{
    logger.log("Matrix:: Swap");
    int frst = this->getElementAtPosition(i, j, true);
    int scnd = this->getElementAtPosition(j, i, false);
    writeElement(frst, j, i, false);
    writeElement(scnd, i, j, false);
    return;
}
void Matrix::transpose()
{
    logger.log("Matrix::TRANSPOSE");
    long long int n = this->columnCount;
    long long int i, j;
    firstPage = PageMatrix(this->matrixName, firstPageNumber);

    for (i = 0; i < n; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            swap(i, j);
        }
    }
    return;
}
