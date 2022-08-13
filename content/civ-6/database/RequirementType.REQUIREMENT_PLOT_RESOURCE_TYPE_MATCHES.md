---
tags:
- RequirementType
title: REQUIREMENT_PLOT_RESOURCE_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_RESOURCE_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* ResourceType `String`
>		* [Resources.ResourceType]

## Samples

```SQL {title="REQUIREMENT_BUILDING_DISCOUNT_RESOURCE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_BUILDING_DISCOUNT_RESOURCE",
		"REQUIREMENT_PLOT_RESOURCE_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIREMENT_BUILDING_DISCOUNT_RESOURCE",
		"ResourceType",
		"RESOURCE_GYPSUM,
        RESOURCE_MARBLE,"
	);
	
```
