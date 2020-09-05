#ifndef LOGGER
#include "logger.h"
#define LOGGER
#endif
/**
 * @brief The PageMatrix object is the main memory representation of a physical page
 * (equivalent to a block). The page class and the page.h header file are at the
 * bottom of the dependency tree when compiling files. 
 *<p>
 * Do NOT modify the PageMatrix class. If you find that modifications
 * are necessary, you may do so by posting the change you want to make on Moodle
 * or Teams with justification and gaining approval from the TAs. 
 *</p>
 */

class PageMatrix
{

    string matrixName;
    string pageIndex;
    vector<int> values;
    uint pageSize;

public:
    string pageName = "";
    PageMatrix();
    PageMatrix(string matrixName, int pageIndex);
    PageMatrix(string matrixName, int pageIndex, vector<int> values, uint pageSize);
    vector<int> getValues();
    void setValues(vector<int> values);
    void writePage();
    
};