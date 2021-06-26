;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!
;;
;; Here are some additional functions/macros that could help you configure Doom:
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.

;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets.
(setq user-full-name "Foster Hangdaan"
      user-mail-address "foster.hangdaan@gmail.com")

;; Doom exposes five (optional) variables for controlling fonts in Doom. Here
;; are the three important ones:
;;
;; + `doom-font'
;; + `doom-variable-pitch-font'
;; + `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;;
;; They all accept either a font-spec, font string ("Input Mono-12"), or xlfd
;; font string. You generally only need these two:
;; (setq doom-font (font-spec :family "monospace" :size 12 :weight 'semi-light)
;;       doom-variable-pitch-font (font-spec :family "sans" :size 13))
;;
;;(setq doom-font (font-spec :family "FiraCode Nerd Font" :size 15)
(setq doom-font (font-spec :family "CaskaydiaCove Nerd Font Mono" :size 15)
      doom-variable-pitch-font (font-spec :family "Ubuntu" :size 15)
      doom-big-font (font-spec :family "CaskaydiaCove Nerd Font Mono" :size 24))

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-dracula)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
;;(setq display-line-numbers-type t)
(setq display-line-numbers-type 'visual)

;; Enable text wrap
(setq-default truncate-lines nil)

;; ****************
;; TAB CONFIG
;; ****************
;; Create a variable for our preferred tab width
(setq custom-tab-width 2)

;; Set default tab display width
(setq-default tab-width custom-tab-width)

;; Allow indentation to insert tabs only
(setq-default indent-tabs-mode t)

;; Make tab key always call an indent command
(setq-default tab-always-indent t)

;; Language specific tweaks
(setq-default typescript-indent-level custom-tab-width)
(setq-default python-indent custom-tab-width)
(setq-default web-mode-markup-indent-offset custom-tab-width)
(setq-default web-mode-css-indent-offset custom-tab-width)
(setq-default web-mode-code-indent-offset custom-tab-width)

;; ************
;; VTERM CONFIG
;; ************
(setq vterm-shell "/bin/fish")

;; ***********
;; Keybindings
;; ***********

;; Evil Multi-edit
;; ---------------
(defun evil-multiedit-default-keybinds ()
  ;; Highlights all matches of the selection in the buffer
  (define-key evil-visual-state-map "R" #'evil-multiedit-match-all)

  ;; Match the word under cursor (i.e. make it an edit region). Consecutive presses
  ;; will incrementally add the next unmatched match.
  (define-key evil-normal-state-map (kbd "M-d") #'evil-multiedit-match-and-next)
  ;; Match selected region
  (define-key evil-visual-state-map (kbd "M-d") #'evil-multiedit-match-and-next)
  ;; Insert marker at point
  (define-key evil-insert-state-map (kbd "M-d") #'evil-multiedit-toggle-marker-here)

  ;; Same as M-d but in reverse
  (define-key evil-normal-state-map (kbd "M-D") #'evil-multiedit-match-and-prev)
  (define-key evil-visual-state-map (kbd "M-D") #'evil-multiedit-match-and-prev)

  ;; OPTIONAL: If you prefer to grab symbols rather than words, use
  ;; `evil-multiedit-match-symbol-and-next' (or prev)

  ;; Restore the last group of multiedit regions
  (define-key evil-visual-state-map (kbd "C-M-D") #'evil-multiedit-restore)

  ;; RET will toggle the region under the cursor
  (define-key evil-multiedit-state-map (kbd "RET") #'evil-multiedit-toggle-or-restrict-region)

  ;; ...and in visual mode, RET will disable all fields outside the selected region
  (define-key evil-motion-state-map (kbd "RET") #'evil-multiedit-toggle-or-restrict-region)

  ;; For moving between edit regions
  (define-key evil-multiedit-state-map (kbd "C-n") #'evil-multiedit-next)
  (define-key evil-multiedit-state-map (kbd "C-p") #'evil-multiedit-prev)
  (define-key evil-multiedit-insert-state-map (kbd "C-n") #'evil-multiedit-next)
  (define-key evil-multiedit-insert-state-map (kbd "C-p") #'evil-multiedit-prev)

  ;; Ex command that allows you to invoke evil-multiedit with a regular expression
  (evil-ex-define-cmd "ie[dit]" #'evil-multiedit-ex-match))
