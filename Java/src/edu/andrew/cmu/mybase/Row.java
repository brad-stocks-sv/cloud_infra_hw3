package edu.andrew.cmu.mybase;

import java.util.ArrayList;
import java.util.List;


/**
 * The class for row in the MyBase.
 * @author songzhaoxiong
 */
public class Row implements Comparable<Row>{
    /**
     * Row key for the table entry.
     */
    private String rowKey;
    /**
     * Container for column families in a row.
     */
    private List<ColumnFamily> columnFamilies;

    /**
     * General constructor.
     * @param rowKey key for the row
     */
    public Row(String rowKey) {
        this.rowKey = rowKey;
        columnFamilies = new ArrayList<>();
    }

    /**
     * Constructor with pre-created column cells.
     * For simplicity, I do not make safe copy for the underlying container.
     * @param rowKey key for the row
     * @param columnFamilies all the column families in the row
     */
    public Row(String rowKey, List<ColumnFamily> columnFamilies) {
        this.rowKey = rowKey;
        this.columnFamilies = columnFamilies;
    }

    public String getRowKey() {
        return rowKey;
    }

    public void setRowKey(String rowKey) {
        this.rowKey = rowKey;
    }

    public List<ColumnFamily> getColumnFamilies() {
        return columnFamilies;
    }

    public void setColumnFamilies(List<ColumnFamily> columnFamilies) {
        this.columnFamilies = columnFamilies;
    }

    /**
     * This method compares the rows in a table.
     * The comparision is done in lexicographical order.
     * @param row the row to compare with
     * @return the relationship between two rows
     */
    @Override
    public int compareTo(Row row) {
        return this.rowKey.compareTo(row.getRowKey());
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
        Row row = (Row)obj;
        if (!this.getRowKey().equals(row.getRowKey())) {
            return false;
        }
        return true;
    }
}
