import styles from "../../styles/Sidebar.module.css";

type NavItem = {
  label: string;
  href?: string;
  active?: boolean;
};

type SidebarProps = {
  title?: string;
  items: NavItem[];
  open?: boolean;
};

export function Sidebar({ title, items, open = true }: SidebarProps) {
  return (
    <aside className={`${styles.sidebar} ${open ? styles.open : styles.closed}`}>
      {title && <div className={styles.title}>{title}</div>}
      <nav className={styles.nav}>
        {items.map((item) => (
          <a key={item.label} href={item.href ?? "#"} className={`${styles.item} ${item.active ? styles.active : ""}`}>
            {item.label}
          </a>
        ))}
      </nav>
    </aside>
  );
}
