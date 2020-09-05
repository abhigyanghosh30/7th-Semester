#include "global.h"
/**
 * @brief 
 * SYNTAX: LOAD relation_name
 */
bool syntacticParseLOAD()
{
    logger.log("syntacticParseLOAD");
    if (tokenizedQuery.size() != 2 && tokenizedQuery.size()!=3)
    {
        cout << "SYNTAX ERROR" << endl;
        return false;
    }
    parsedQuery.queryType = LOAD;
    if(tokenizedQuery.size() == 2)
    {
        parsedQuery.loadRelationName = tokenizedQuery[1];\
        IS_MATRIX = false;
    }
    else if (tokenizedQuery[1] == "MATRIX")
        {
            parsedQuery.loadRelationName = tokenizedQuery[2];
            IS_MATRIX = true;
        }
    else
    {
        cout<<"SYNTAX ERROR \n";
        return false;
    }
    
        
    return true;
}

bool semanticParseLOAD()
{
    logger.log("semanticParseLOAD");
    if(IS_MATRIX)
    {
        if(matrixCatalogue.isMatrix(parsedQuery.loadRelationName))
        {
            cout << "SEMANTIC ERROR: Matrix already exists" << endl;
            return false;
        }
         if (!isFileExists(parsedQuery.loadRelationName))
        {
            cout << "SEMANTIC ERROR: Data file doesn't exist" << endl;
            return false;
        }
    }
    else
    {
        if (tableCatalogue.isTable(parsedQuery.loadRelationName))
        {
            cout << "SEMANTIC ERROR: Relation already exists" << endl;
            return false;
        }

        if (!isFileExists(parsedQuery.loadRelationName))
        {
            cout << "SEMANTIC ERROR: Data file doesn't exist" << endl;
            return false;
        }
    }
    
 
    return true;
}

void executeLOAD()
{
    logger.log("executeLOAD");

    if(IS_MATRIX)
    {
        Matrix *matrix = new Matrix(parsedQuery.loadRelationName);
        if (matrix->load())
        {
            matrixCatalogue.insertMatrix(matrix);
            cout << "Loaded Matrix. Column Count: " << matrix->columnCount << " Row Count: " << matrix->columnCount << endl;
        }
        return ;
    }
    Table *table = new Table(parsedQuery.loadRelationName);
    if (table->load())
    {
        tableCatalogue.insertTable(table);
        cout << "Loaded Table. Column Count: " << table->columnCount << " Row Count: " << table->rowCount << endl;
    }
    return;
}