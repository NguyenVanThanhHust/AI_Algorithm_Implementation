#pragma once
#include <vector>
#include "olcPixelGameEngine.h"

class PathFinding : public olcPixelGameEngine
{
public:
        PathFinding();
        {
            m_sAppName = L"PathFinding";
        } 

        bool OnUserCreate() override
        {
            // create map of nodes
            nodes = new sNode[nMapWidth * nMapHeight];
            for (int i = 0; i < nMapWidth; i++)
            {
                for (int j = 0; j < nMapHeight; j++)
                {
                    nodes[j * nMapWidth + i].x = i;
                    nodes[j * nMapWidth + i].y = j;
                    nodes[j * nMapWidth + i].bObstacle = false;
                    nodes[j * nMapWidth + i].parent = nullptr;
                    nodes[j * nMapWidth + i].bVisited = false;
                }
            }
        }
private:
    struct sNode
    {
        bool bObstacle; // true if the node is a obstacle
        bool bVisited; // true if the node is visited
        float fGlobalGoal; // distance to goal
        float fLocalGoal; // distance to goal if we took to the alternative path
        int x; // Node position in 2d space
        int y; 
        std::vector<sNode> vecNeighbours; // connection to neighbours
        sNode* parent;
    }

    // create list of nodes 
    sNode *nodes = nullptr;
    int nMapWidth = 16;
    int nMapHeight = 16;

protected:
    virtual bool OnUserCreate()


}
int main(int argc, char)
{
    One
}