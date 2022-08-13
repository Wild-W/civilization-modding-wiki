---
tags:
- RequirementType
title: REQUIREMENT_PLOT_FEATURE_TAG_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_FEATURE_TAG_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* Tag `String`

## Samples

```SQL {title="REQUIRES_PLOT_HAS_FLOODPLAINS_TAG"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLOT_HAS_FLOODPLAINS_TAG",
		"REQUIREMENT_PLOT_FEATURE_TAG_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLOT_HAS_FLOODPLAINS_TAG",
		"Tag",
		"CLASS_FLOODPLAINS"
	);
	
```
