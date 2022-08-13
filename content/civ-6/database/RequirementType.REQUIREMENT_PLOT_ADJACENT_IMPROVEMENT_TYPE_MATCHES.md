---
tags:
- RequirementType
title: REQUIREMENT_PLOT_ADJACENT_IMPROVEMENT_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_ADJACENT_IMPROVEMENT_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]

## Samples

```SQL {title="REQUIRES_PLOT_ADJACENT_CHATEAU"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLOT_ADJACENT_CHATEAU",
		"REQUIREMENT_PLOT_ADJACENT_IMPROVEMENT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLOT_ADJACENT_CHATEAU",
		"ImprovementType",
		"IMPROVEMENT_CHATEAU"
	);
	
```
