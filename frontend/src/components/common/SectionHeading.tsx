import styles from "../../styles/SectionHeading.module.css";

type SectionHeadingProps = {
  title: string;
  description?: string;
  eyebrow?: string;
};

export function SectionHeading({ title, description, eyebrow }: SectionHeadingProps) {
  return (
    <div className={styles.heading}>
      {eyebrow && <p className={styles.eyebrow}>{eyebrow}</p>}
      <div>
        <h2 className={styles.title}>{title}</h2>
        {description && <p className={styles.description}>{description}</p>}
      </div>
    </div>
  );
}
