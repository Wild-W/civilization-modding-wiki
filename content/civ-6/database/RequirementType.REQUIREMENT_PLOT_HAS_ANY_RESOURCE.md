---
tags:
- RequirementType
title: REQUIREMENT_PLOT_HAS_ANY_RESOURCE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_HAS_ANY_RESOURCE
>
> * Class: `PLOTS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="PLOT_HAS_RESOURCE_REQUIREMENTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLOT_HAS_RESOURCE_REQUIREMENTS",
		"REQUIREMENT_PLOT_HAS_ANY_RESOURCE"
	);


```
