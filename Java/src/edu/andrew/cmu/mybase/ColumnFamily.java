package edu.andrew.cmu.mybase;

import java.util.ArrayList;
import java.util.List;

/**
 * Class for column family in a specific row
 * @author songzhaoxiong
 */
public class ColumnFamily {
    /**
     * Key for the column family.
     */
    private String columnFamilyQualifier;
    /**
     * All the column cells in this column family
     */
    private List<Column> columns;

    /**
     * General constructor.
     * @param columnFamilyQualifier key for the column family
     */
    public ColumnFamily(String columnFamilyQualifier) {
        this.columnFamilyQualifier = columnFamilyQualifier;
        // Initial design we stay with array implementation.
        columns = new ArrayList<>();
    }

    /**
     * Constructor with already created cells.
     * @param columnFamilyQualifier key for the column family
     * @param columns columns for the column family
     */
    public ColumnFamily(String columnFamilyQualifier, List<Column> columns) {
        this.columnFamilyQualifier = columnFamilyQualifier;
        this.columns = columns;
    }

    public String getColumnFamilyQualifier() {
        return columnFamilyQualifier;
    }

    public void setColumnFamilyKey(String columnFamilyKey) {
        this.columnFamilyQualifier = columnFamilyKey;
    }

    public List<Column> getColumns() {
        return columns;
    }

    public void setColumns(List<Column> columns) {
        this.columns = columns;
    }

    /**
     * In this project, null reference only equals to null.
     * @param obj object to compare with
     * @return whether this two objects are equal
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (this.getClass() != obj.getClass()) {
            return false;
        }
        ColumnFamily columnFamily = (ColumnFamily)obj;
        if (!this.getColumnFamilyQualifier().equals(getColumnFamilyQualifier())) {
            return false;
        }
        return true;
    }
}
