import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "█ LLM WIKI",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "ko-KR",
    baseUrl: "example.github.io/llm-wiki",
    ignorePatterns: ["private", "_templates", "90-Archive", ".obsidian", ".trash", "CLAUDE.md"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Pretendard Variable",
        body: "Pretendard Variable",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#f0efe9",
          lightgray: "#d8d6cc",
          gray: "#8a887e",
          darkgray: "#333333",
          dark: "#111111",
          secondary: "#111111",
          tertiary: "#7c5cff",
          highlight: "rgba(214, 255, 63, 0.35)",
          textHighlight: "#d6ff3f",
        },
        darkMode: {
          light: "#111111",
          lightgray: "#2a2a2a",
          gray: "#7a7a72",
          darkgray: "#d8d6cc",
          dark: "#f0efe9",
          secondary: "#f0efe9",
          tertiary: "#9d85ff",
          highlight: "rgba(214, 255, 63, 0.15)",
          textHighlight: "#d6ff3f",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.ExplicitPublish()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Commented out: "Pretendard Variable" is not a Google Fonts family, so
      // fontOrigin: "googleFonts" cannot fetch it for satori-based OG image
      // rendering and the build fails. Re-enable once local font files are
      // vendored (fontOrigin: "local") or a Google-Fonts-hosted fallback is chosen.
      // Plugin.CustomOgImages(),
    ],
  },
}

export default config
