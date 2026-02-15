---
name: ocr-workflow
description: Process documents through OCR pipeline - upload, extract text, validate output. Use when working with OCR, document processing, text extraction, PDF/image scanning, Paperless-ngx parsers, or West African document formats (French, local scripts).
---

# OCR Workflow

## Paperless-ngx Parsers (OCT Foundation)

| Parser | Location | Use Case |
|--------|----------|----------|
| Tesseract | `src/paperless_tesseract/` | Rasterised images, scanned PDFs |
| OCRmyPDF | `ocrmypdf` (pyproject) | PDFs—adds searchable layer |
| Tika | `src/paperless_tika/` | Apache Tika extraction |
| Azure | `azure-ai-documentintelligence` | Cloud OCR |
| Text | `src/paperless_text/` | Plain text files |

Document parser base: `documents.parsers.DocumentParser`. Parsers implement `parse()`, `get_thumbnail()`.

## Document Processing Pipeline

1. **Ingest**: Validate file type (PDF, PNG, JPEG, TIFF)
2. **Preprocess**: Deskew, denoise, binarize if needed for scanned docs
3. **Extract**: Run OCR engine (Tesseract, OCRmyPDF, or Azure)
4. **Postprocess**: Clean output, handle multi-page, language detection
5. **Validate**: Confidence threshold, empty-result handling

## West Africa Considerations

- **Languages**: French, English, Arabic, local scripts (e.g., N'Ko, Vai)
- **Document types**: Government IDs, bank statements, handwritten forms, printed receipts
- **Quality**: Variable scan quality; preprocessing critical
- **Tesseract**: Add language packs (fra, eng, ara) in Docker/config

## Key Code Paths

- `src/paperless_tesseract/parsers.py` - RasterisedDocumentParser (Tesseract)
- `src/documents/parsers.py` - Parser registry, DocumentParser base
- `paperless.config.OcrConfig` - OCR settings (languages, mode)
