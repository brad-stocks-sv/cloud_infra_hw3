package edu.andrew.cmu.mybase;

import java.util.Set;
import java.util.TreeSet;

/**
 * In memory table data structure.
 * Memtable actually is the SStable in memory.
 * The initial implementation, I use TreeSet to facilitate fast search.
 * Writing would be little bit slow than search but we need only 10% of update of
 * all inputs.
 * @author songzhaoxiong
 */
public class Memtable {
    /**
     * Initial maximum size for the Memtable.
     */
    private long maxSize;
    /**
     * Aggregate of rows in the Memtable.
     */
    private Set<Row> rows;

    /**
     * Constructor with maximum size passed in.
     * @param maxSize the maximum size for in memory data structure
     */
    public Memtable(long maxSize) {
        this.maxSize = maxSize;
        rows = new TreeSet<>();
    }

    /**
     * Constructor with pre-created set of rows.
     * @param maxSize the maximum size for in memory data structure
     * @param rows pre-created set of rows.
     */
    public Memtable(long maxSize, Set<Row> rows) {
        this.maxSize = maxSize;
        this.rows = rows;
    }
}
