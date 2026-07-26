import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { FullSlug, resolveRelative } from "../util/path"
import { classNames } from "../util/lang"

const LanguageToggle: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const translation = fileData.frontmatter?.translation as FullSlug | undefined
  if (!translation) {
    return null
  }

  const lang = fileData.frontmatter?.lang as string | undefined
  const label = lang === "en" ? "한국어" : "EN"
  const href = resolveRelative(fileData.slug!, translation)

  return (
    <a href={href} class={classNames(displayClass, "language-toggle")}>
      {label}
    </a>
  )
}

export default (() => LanguageToggle) satisfies QuartzComponentConstructor
