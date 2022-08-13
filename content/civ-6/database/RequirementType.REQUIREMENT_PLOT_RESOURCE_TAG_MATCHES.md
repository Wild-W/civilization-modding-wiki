---
tags:
- RequirementType
title: REQUIREMENT_PLOT_RESOURCE_TAG_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_RESOURCE_TAG_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* Tag `String`

## Samples

```SQL {title="REQUIRES_PLOT_HAS_TAG_GODDESS_OF_FESTIVAL"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLOT_HAS_TAG_GODDESS_OF_FESTIVAL",
		"REQUIREMENT_PLOT_RESOURCE_TAG_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLOT_HAS_TAG_GODDESS_OF_FESTIVAL",
		"Tag",
		"CLASS_GODDESS_OF_FESTIVALS"
	);
	
```
