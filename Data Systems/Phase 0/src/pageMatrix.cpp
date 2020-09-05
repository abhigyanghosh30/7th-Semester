#include "global.h"
/**
 * @brief Construct a new PageMatrix object. Never used as part of the code
 *
 */
PageMatrix::PageMatrix()
{
    this->pageName = "";
    this->matrixName = "";
    this->pageIndex = -1;
    this->pageSize = 0;
}

/**
 * @brief Construct a new PageMatrix:: PageMatrix object given the matrix name and page
 * index. When matrixs are loaded they are broken up into blocks of BLOCK_SIZE
 * and each block is stored in a different file named
 * "<matrixname>_Page<pageindex>". For example, If the PageMatrix being loaded is of
 * matrix "R" and the pageIndex is 2 then the file name is "R_Page2". The page
 * loads the rows (or tuples) into a vector of rows (where each row is a vector
 * of integers).
 *
 * @param matrixName 
 * @param pageIndex 
 */
PageMatrix::PageMatrix(string matrixName, int pageIndex)
{
    logger.log("PageMatrix::PageMatrix");
    this->matrixName = matrixName;
    this->pageIndex = pageIndex;
    this->pageName = "../data/temp/" + this->matrixName + "_Page" + to_string(pageIndex);
    this->pageSize = 256;
    Matrix matrix = *matrixCatalogue.getMatrix(matrixName);
    vector<int> values;
    logger.log("PageMatrix::PageMatrix here");

    ifstream fin(pageName, ios::in);
    int number;
    while(fin >> number)
    {
        // fin >> number;
        // cout<<"Number: " <<number<<" "<<"Page Size: "<<this->pageSize<<endl;
        values.push_back(number);
    }
    this->values = values;
    logger.log("PageMatrix::PageMatrix there");

    fin.close();
    logger.log("PageMatrix::PageMatrix");

}

/**
 * @brief Get row from page indexed by rowIndex
 * 
 * @param rowIndex 
 * @return vector<int> 
 */
vector<int> PageMatrix::getValues()
{
    logger.log("PageMatrix::getRow");
    // cout<<"Values in the page: "<<this->values.size()<<endl;
    return this->values;
}
void PageMatrix::setValues(vector<int> values)
{
    logger.log("PageMatrix::Set Row");
    this->values = values;
}
PageMatrix::PageMatrix(string matrixName, int pageIndex, vector<int> values, uint pageSize)
{
    logger.log("PageMatrix::PageMatrix");
    this->matrixName = matrixName;
    this->pageIndex = pageIndex;
    this->values = values;
    this->pageSize = pageSize;
    this->pageName = "../data/temp/" + this->matrixName + "_Page" + to_string(pageIndex);
}

/**
 * @brief writes current page contents to file.
 * 
 */
void PageMatrix::writePage()
{
    logger.log("PageMatrix::writePage");
    ofstream fout(this->pageName, ios::trunc);
    for (vector<int>::iterator it = this->values.begin(); it != this->values.end(); it++)
    {
        if (it != values.begin())
            fout << " ";
        fout << *it;
    }
    fout << endl;
    fout.close();
}
