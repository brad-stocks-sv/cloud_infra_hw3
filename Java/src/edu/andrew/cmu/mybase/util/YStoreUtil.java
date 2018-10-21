package edu.andrew.cmu.mybase.util;

import edu.andrew.cmu.mybase.Row;

import java.io.File;
import java.util.Set;

/**
 * A utility class to handle YStore.
 * When spilling the Memtable, instead of implementing the sophisticated
 * LSM-Tree merging process. We read in all the YStore file into memory and merge
 * it with Memtable.
 * @author songzhaoxiong
 */
public class YStoreUtil {
    /**
     * This method parse the YStore into a set of rows.
     * @param path
     * @return
     */
    public Set<Row> parser(File path) {
        return null;
    }
}
