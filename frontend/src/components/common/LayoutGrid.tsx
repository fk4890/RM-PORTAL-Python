import styles from "../../styles/LayoutGrid.module.css";

type LayoutGridProps = {
  children: React.ReactNode;
  columns?: number; // 推奨カラム数の目安（実際は auto-fit で調整）
};

export function LayoutGrid({ children, columns = 2 }: LayoutGridProps) {
  const minWidth = columns >= 4 ? 180 : columns === 3 ? 200 : 240;
  return (
    <div className={styles.grid} style={{ gridTemplateColumns: `repeat(auto-fit, minmax(${minWidth}px, 1fr))` }}>
      {children}
    </div>
  );
}
