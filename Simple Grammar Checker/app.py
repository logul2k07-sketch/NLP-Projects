from grammar_checker import analyze_sentence, check_grammar, correct_text, highlight_errors


def display_errors(errors, text):
    if not errors:
        print("\n✅ No grammar errors found!")
        return
    print(f"\n❌ Found {len(errors)} issue(s):\n")
    for i, error in enumerate(errors, 1):
        print(f"  {i}. {error['message']}")
        print(f"     Context : {error['context']}")
        if error["suggestions"]:
            print(f"     Suggestions: {', '.join(error['suggestions'])}")
        print()

    highlighted = highlight_errors(text, errors)
    print(f"  Highlighted: {highlighted}\n")


def display_tokens(tokens):
    print("\n📝 Token Analysis:")
    print(f"  {'Token':<15} {'POS':<12} {'Dependency'}")
    print("  " + "-" * 40)
    for token, pos, dep in tokens:
        print(f"  {token:<15} {pos:<12} {dep}")


def main():
    print("=" * 50)
    print("    Simple Grammar Checker (NLP-Powered)")
    print("=" * 50)
    print("Commands: 'quit' to exit, 'tokens' to toggle token view\n")

    show_tokens = False

    while True:
        text = input("Enter sentence: ").strip()

        if not text:
            continue
        if text.lower() == "quit":
            print("Goodbye!")
            break
        if text.lower() == "tokens":
            show_tokens = not show_tokens
            print(f"Token view {'enabled' if show_tokens else 'disabled'}.\n")
            continue

        errors = check_grammar(text)
        display_errors(errors, text)

        if errors:
            corrected = correct_text(text)
            if corrected != text:
                print(f"  ✏️  Corrected: {corrected}\n")

        if show_tokens:
            tokens = analyze_sentence(text)
            display_tokens(tokens)

        print()


if __name__ == "__main__":
    main()
