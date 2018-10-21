package edu.andrew.cmu.mybase;

/**
 * Class for columns in the column family.
 * @author songzhaoxiong
 */
public class Column {
    /**
     * Qualifier for this column.
     */
    private String qualifier;
    /**
     * Value for this column;
     */
    private String value;

    /**
     * General constructor
     * @param qualifier key of the cell
     * @param value value of the cell
     */
    public Column(String qualifier, String value) {
        this.qualifier = qualifier;
        this.value = value;
    }

    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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
        Column column = (Column)obj;
        if (!this.getQualifier().equals(column.getQualifier())) {
            return false;
        }
        if (!this.getValue().equals(column.getValue())) {
            return false;
        }
        return true;
    }
}
