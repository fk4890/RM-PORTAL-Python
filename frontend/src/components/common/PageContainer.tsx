import { PageHeader } from "./PageHeader";

type PageContainerProps = {
  title: string;
  subtitle?: string;
  badge?: string;
  className?: string;
  children: React.ReactNode;
};

export function PageContainer({ title, subtitle, badge, className, children }: PageContainerProps) {
  return (
    <main className={className}>
      <PageHeader title={title} subtitle={subtitle} badge={badge} />
      {children}
    </main>
  );
}
