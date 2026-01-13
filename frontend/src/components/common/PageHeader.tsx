import styles from "../../styles/PageHeader.module.css";
import badgeStyles from "../../styles/Badge.module.css";
import textStyles from "../../styles/Text.module.css";

type PageHeaderProps = {
  title: string;
  subtitle?: string;
  badge?: string;
  className?: string;
};

export function PageHeader({ title, subtitle, badge, className }: PageHeaderProps) {
  return (
    <header className={`${styles.header} ${className ?? ""}`.trim()}>
      <div>
        {subtitle && (
          <p className={textStyles.textMuted} style={{ margin: 0 }}>
            {subtitle}
          </p>
        )}
        <h1 className={styles.title}>{title}</h1>
      </div>
      {badge && <span className={badgeStyles.badgePrimary}>{badge}</span>}
    </header>
  );
}
