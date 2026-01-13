import styles from "../../styles/DataTable.module.css";

type DataTableProps = {
  columns: string[];
  rows: Array<Record<string, string>>;
  caption?: string;
  onRowClick?: (row: Record<string, string>) => void;
};

export function DataTable({ columns, rows, caption, onRowClick }: DataTableProps) {
  return (
    <div className={styles.table}>
      {caption && <div className={styles.caption}>{caption}</div>}
      <table className={styles.tableInner}>
        <thead>
          <tr>
            {columns.map((col) => (
              <th key={col} className={styles.th}>
                {col}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, idx) => (
            <tr
              key={idx}
              className={onRowClick ? styles.clickable : undefined}
              onClick={() => {
                if (onRowClick) onRowClick(row);
              }}
            >
              {columns.map((col) => (
                <td key={col} className={styles.td}>
                  {row[col] ?? "-"}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
