"use client";

import { useState } from "react";
import styles from "../../styles/BaseLayout.module.css";
import { Header } from "./Header";
import { Sidebar } from "./Sidebar";

type NavItem = {
  label: string;
  href?: string;
  active?: boolean;
};

type BaseLayoutProps = {
  title: string;
  userName?: string;
  navTitle?: string;
  navItems: NavItem[];
  actions?: React.ReactNode;
  children: React.ReactNode;
};

export function BaseLayout({ title, userName, navTitle, navItems, actions, children }: BaseLayoutProps) {
  const [open, setOpen] = useState(true);
  const toggle = () => setOpen((prev) => !prev);

  return (
    <div className={styles.appshell}>
      <Sidebar title={navTitle} items={navItems} open={open} />
      <div className={`${styles.body} ${open ? styles.bodyWithNav : ""}`}>
        <Header title={title} userName={userName} onToggleMenu={toggle} actions={<>{actions}</>} />
        <div className={styles.content}>{children}</div>
      </div>
    </div>
  );
}
