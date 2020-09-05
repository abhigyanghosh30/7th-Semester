#include "global.h"

/**
 * @brief 
 * SYNTAX: R <- TRANSPOSE relation_name 
 */
bool syntacticParseTRANSPOSE()
{
    logger.log("syntacticParseTRANSPOSE");
    if (tokenizedQuery.size() != 2)
    {
        cout << "SYNTAX ERROR" << endl;
        return false;
    }
    parsedQuery.queryType = TRANSPOSE;
    parsedQuery.transposeName = tokenizedQuery[1];
    return true;
}

bool semanticParseTRANSPOSE()
{
    logger.log("semanticParseTRANSPOSE");
    if (matrixCatalogue.isMatrix(parsedQuery.transposeName))
    {
        return true;
    }
    cout<<"MATRIX NOT FOUND\n";
    return false;
}

void executeTRANSPOSE()
{
    logger.log("executeTRANSPOSE");

    Matrix* matrix = matrixCatalogue.getMatrix(parsedQuery.transposeName);
    matrix->transpose();

    return;
}