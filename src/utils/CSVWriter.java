package utils;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class CSVWriter {
    /**
     * Add line to CSV
     * Created using tutorial: https://www.baeldung.com/java-csv
     * @param data String array to be converted to line for csv file
     * @param csvFileName CSV file to be appended to
     * @throws IOException CSV file could not be opened
     */
    public static void appendCSV(String[] data, String csvFileName) throws IOException {
        File csvOutputFile = new File(csvFileName);
        try (PrintWriter pw = new PrintWriter(new FileOutputStream(csvOutputFile, true))) {
            String newLine = CSVWriter.convertToCSV(data);
            pw.println(newLine);
        }
    }

    /**
     * Remove a certain row from a CSV file.
     * @param rowNum Row number to remove (0-indexed). Works with negative indexing.
     * @param csvFileName  CSV file to be modified 
     * @throws IOException CSV file does not exist
     */
    public static void removeRow(int rowNum, String csvFileName) throws IOException {
        List<List<String>> data = CSVReader.readCSV(csvFileName);
        if (rowNum < 0) {
            rowNum = data.size() + rowNum;
        }
        data.remove(rowNum);
        File csvOutputFile = new File(csvFileName);
        try (PrintWriter pw = new PrintWriter(new FileOutputStream(csvOutputFile, false))) {
            for (List<String> line: data) {
                String newLine = CSVWriter.convertToCSV(line.toArray(String[]::new));
                pw.println(newLine);
            }
        }
    }

    /**
     * Convert string array to csv format
     * Created using tutorial: https://www.baeldung.com/java-csv
     * @param data String array to be converted to line for csv file
     * @return String as comma concatenated version of data with special characters escaped
     */
    private static String convertToCSV(String[] data) {
        return Stream.of(data)
        .map(CSVWriter::escapeSpecialCharacters)
        .collect(Collectors.joining(","));
    }

    /**
     * Remove special characters from string by ecsaping them
     * Created using tutorial: https://www.baeldung.com/java-csv
     * @param data String to be formatted
     * @return Formatted version of string
     */
    private static String escapeSpecialCharacters(String data) {
        if (data == null) {
            throw new IllegalArgumentException("Input data cannot be null");
        }
        String escapedData = data.replaceAll("\\R", " ");
        if (data.contains(",") || data.contains("\"") || data.contains("'")) {
            data = data.replace("\"", "\"\"");
            escapedData = "\"" + data + "\"";
        }
        return escapedData;
    }
}
