import json
from pathlib import Path


class ReportWriter:

    def __init__(self):
        Path("reports").mkdir(exist_ok=True)

    def save_json(self, call_id, report):

        filename = Path("reports") / f"{call_id}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

        return filename

    def save_markdown(self, call_id, report):

        filename = Path("reports") / f"{call_id}.md"

        with open(filename, "w", encoding="utf-8") as f:

            f.write(f"# Call Report: {call_id}\n\n")

            f.write(f"## Summary\n")
            f.write(f"{report.get('summary', 'No summary available')}\n\n")

            f.write(f"## Overall Score\n")
            f.write(f"{report.get('overall_score', 0)}/100\n\n")

            f.write(f"## Call Successful\n")
            f.write(
                f"{report.get('call_successful', False)}\n\n"
            )

            issues = report.get("issues", [])

            f.write(f"## Issues Found\n\n")

            if not issues:
                f.write("No issues detected.\n")
            else:

                for issue in issues:

                    f.write(
                        f"### {issue.get('issue_id', 'BUG-UNKNOWN')}\n"
                    )

                    f.write(
                        f"**Severity:** {issue.get('severity', 'UNKNOWN')}\n\n"
                    )

                    f.write(
                        f"**Category:** {issue.get('category', 'UNKNOWN')}\n\n"
                    )

                    f.write(
                        f"**Description:**\n"
                        f"{issue.get('description', '')}\n\n"
                    )

                    f.write(
                        f"**Recommendation:**\n"
                        f"{issue.get('recommendation', '')}\n\n"
                    )

                    f.write("---\n\n")

        return filename

    def save_all(self, call_id, report):

        json_file = self.save_json(
            call_id,
            report
        )

        md_file = self.save_markdown(
            call_id,
            report
        )

        return {
            "json": str(json_file),
            "markdown": str(md_file)
        }