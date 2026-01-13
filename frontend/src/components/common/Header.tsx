import styles from "../../styles/Header.module.css";

type HeaderProps = {
  title: string;
  userName?: string;
  actions?: React.ReactNode;
  onToggleMenu?: () => void;
};

export function Header({ title, userName, actions, onToggleMenu }: HeaderProps) {
  return (
    <header className={styles.header}>
      <div className={styles.left}>
        {onToggleMenu && (
          <button className={styles.menuBtn} onClick={onToggleMenu} aria-label="メニュー切替">
            ☰
          </button>
        )}
        <div className={styles.title}>{title}</div>
      </div>
      <div className={styles.right}>
        {actions}
        {userName && <div className={styles.user}>{userName}</div>}
      </div>
    </header>
  );
}
