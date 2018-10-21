package edu.andrew.cmu.mybase;

import java.io.File;
import java.util.Map;
import java.util.TreeMap;

/**
 * This is the in-memory handler of the YIndex file.
 * For each spill, YIndex will be regenerated and YIndex will be cached in this
 * class. Simply, all the entries in the YIndex will be loaded into memory.
 */
public class Index {
    /**
     * Path of file for YIndex on the file system.
     * It can also be the name of the table which stores the index.
     */
    private File path;
    /**
     * In-memory index data structure.
     * Here how to track the on-disk entry is not specified. So the value is set
     * to be Object currently.
     * To decrease disk access. When the spill happens, we do this thing:
     * 1. We write to the local file, and we get back the offset.
     * 2. We store the row-offset in commodity database, like MySQL.
     * 3. After the writing in database, we get save the save row-offset pair in this
     * inMemoryIndex. This can save our time to load from disk to memory again.
     */
    private Map<String, Object> inMemoryIndex;

    /**
     * General constructor for index.
     */
    public Index() {
        // The initial version we use tree map.
        inMemoryIndex = new TreeMap<>();
    }
    /**
     * When the table is open, if there is YIndex out there. We cache it in the memory.
     * When spills happens, the YIndex is updated. In the same time update the in-memory index.
     */
    public void cacheIndex() {

    }
}
