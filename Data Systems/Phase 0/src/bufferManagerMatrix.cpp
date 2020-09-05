#include "global.h"

BufferManagerMatrix::BufferManagerMatrix()
{
    logger.log("BufferManagerMatrix::BufferManagerMatrix");
}

/**
 * @brief Function called to read a page from the buffer manager. If the page is
 * not present in the pool, the page is read and then inserted into the pool.
 *
 * @param tableName 
 * @param pageIndex 
 * @return Page 
 */
PageMatrix BufferManagerMatrix::getPage(string tableName, int pageIndex)
{
    logger.log("BufferManagerMatrix::getPage");
    string pageName = "../data/temp/" + tableName + "_Page" + to_string(pageIndex);
    if (this->inPool(pageName))
        return this->getFromPool(pageName);
    else
        return this->insertIntoPool(tableName, pageIndex);
}

/**
 * @brief Checks to see if a page exists in the pool
 *
 * @param pageName 
 * @return true 
 * @return false 
 */
bool BufferManagerMatrix::inPool(string pageName)
{
    logger.log("BufferManagerMatrix::inPool");
    for (auto page : this->pages)
    {
        if (pageName == page.pageName)
            return true;
    }
    return false;
}

/**
 * @brief If the page is present in the pool, then this function returns the
 * page. Note that this function will fail if the page is not present in the
 * pool.
 *
 * @param pageName 
 * @return Page 
 */
PageMatrix BufferManagerMatrix::getFromPool(string pageName)
{
    logger.log("BufferManagerMatrix::getFromPool");
    for (auto page : this->pages)
        if (pageName == page.pageName)
            return page;
}

/**
 * @brief Inserts page indicated by tableName and pageIndex into pool. If the
 * pool is full, the pool ejects the oldest inserted page from the pool and adds
 * the current page at the end. It naturally follows a queue data structure. 
 *
 * @param tableName 
 * @param pageIndex 
 * @return Page 
 */
PageMatrix BufferManagerMatrix::insertIntoPool(string tableName, int pageIndex)
{
    logger.log("BufferManagerMatrix::insertIntoPool");
    PageMatrix page(tableName, pageIndex);
    if (this->pages.size() >= BLOCK_COUNT)
        pages.pop_front();
    pages.push_back(page);
    return page;
}

/**
 * @brief The buffer manager is also responsible for writing pages. This is
 * called when new tables are created using assignment statements.
 *
 * @param tableName 
 * @param pageIndex 
 * @param rows 
 * @param rowCount 
 */
void BufferManagerMatrix::writePage(string tableName, int pageIndex, vector<int> values, uint pageSize)
{
    logger.log("BufferManagerMatrix::writePage");
    PageMatrix page(tableName, pageIndex, values, pageSize);
    page.writePage();
}

/**
 * @brief Deletes file names fileName
 *
 * @param fileName 
 */
void BufferManagerMatrix::deleteFile(string fileName)
{

    if (remove(fileName.c_str()))
        logger.log("BufferManagerMatrix::deleteFile: Err");
    else
        logger.log("BufferManagerMatrix::deleteFile: Success");
}

/**
 * @brief Overloaded function that calls deleteFile(fileName) by constructing
 * the fileName from the tableName and pageIndex.
 *
 * @param tableName 
 * @param pageIndex 
 */
void BufferManagerMatrix::deleteFile(string tableName, int pageIndex)
{
    logger.log("BufferManagerMatrix::deleteFile");
    string fileName = "../data/temp/" + tableName + "_Page" + to_string(pageIndex);
    this->deleteFile(fileName);
}