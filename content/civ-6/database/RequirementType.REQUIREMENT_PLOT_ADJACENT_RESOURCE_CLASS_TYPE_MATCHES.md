---
tags:
- RequirementType
title: REQUIREMENT_PLOT_ADJACENT_RESOURCE_CLASS_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_ADJACENT_RESOURCE_CLASS_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* ResourceClassType `String`
>		* [Resources.ResourceClassType]

## Samples

```SQL {title="REQUIRES_PLOT_ADJACENT_TO_LUXURY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLOT_ADJACENT_TO_LUXURY",
		"REQUIREMENT_PLOT_ADJACENT_RESOURCE_CLASS_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLOT_ADJACENT_TO_LUXURY",
		"ResourceClassType",
		"RESOURCECLASS_LUXURY"
	);
	
```