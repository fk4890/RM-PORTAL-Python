import styles from "../../styles/Card.module.css";

type CardProps = {
  title?: string;
  subtitle?: string;
  children: React.ReactNode;
};

export function Card({ title, subtitle, children }: CardProps) {
  return (
    <div className={styles.card}>
      {(title || subtitle) && (
        <header className={styles.header}>
          {title && <h3 className={styles.title}>{title}</h3>}
          {subtitle && <p className={styles.subtitle}>{subtitle}</p>}
        </header>
      )}
      <div className={styles.body}>{children}</div>
    </div>
  );
}
