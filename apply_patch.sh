#!/usr/bin/env bash
# apply_patch.sh — применяет патч из папки patches/ и удаляет его после успешного применения.
# Использование: ./apply_patch.sh patches/0001-xxx.patch   (или просто имя файла, если он в patches/)
set -e

PATCH="$1"
[ -z "$PATCH" ] && { echo "Использование: $0 <путь/к/патчу>"; exit 1; }
[ ! -f "$PATCH" ] && [ -f "patches/$PATCH" ] && PATCH="patches/$PATCH"
[ ! -f "$PATCH" ] && { echo "Файл не найден: $PATCH"; exit 1; }

if git apply --check "$PATCH" 2>/dev/null; then
    git am --keep-non-patch -q "$PATCH" && echo "✅ Патч применён с коммитом"
else
    echo "⚠️  git am невозможен (патч уже применён или конфликт) — проверяю git apply..."
    git apply --3way "$PATCH" && echo "✅ Патч наложен (без автокоммита)"
fi

rm "$PATCH"
echo "🗑️  Файл $PATCH удалён."
