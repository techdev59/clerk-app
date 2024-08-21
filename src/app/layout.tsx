import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { ClerkProvider } from "@clerk/nextjs";
import AppWrapper from "@/components/Layout/AppWrapper";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Wordpress Hoisting",
  description: "Wordpress hoisting made easy",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body className={inter.className}>
          <AppWrapper>{children}</AppWrapper>
          <div id="modal"></div>
          <script
            type="text/javascript"
            dangerouslySetInnerHTML={{
              __html: `
                window.$crisp=[];
                window.CRISP_WEBSITE_ID="8ee0d6a7-20c5-4b1c-9401-6425163f3671";
                (function(){
                  var d=document;
                  var s=d.createElement("script");
                  s.src="https://client.crisp.chat/l.js";
                  s.async=1;
                  d.getElementsByTagName("head")[0].appendChild(s);
                })();
              `,
            }}
          />
        </body>
      </html>
    </ClerkProvider>
  );
}
