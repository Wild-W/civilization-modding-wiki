---
tags:
- RequirementType
title: REQUIREMENT_PLOT_IMPROVEMENT_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_IMPROVEMENT_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]

## Samples

```SQL {title="REQUIREMENT_CITY_GROWTH_INDUSTRY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_CITY_GROWTH_INDUSTRY",
		"REQUIREMENT_PLOT_IMPROVEMENT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIREMENT_CITY_GROWTH_INDUSTRY",
		"ImprovementType",
		"IMPROVEMENT_INDUSTRY"
	);
	```
