---
tags:
- RequirementType
title: REQUIREMENT_PLOT_ADJACENT_FEATURE_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_ADJACENT_FEATURE_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* FeatureType `String`
>		* [Features.FeatureType]

## Samples

```SQL {title="DEAD_SEA_REQUIRES_ADJACENT_UNIT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"DEAD_SEA_REQUIRES_ADJACENT_UNIT",
		"REQUIREMENT_PLOT_ADJACENT_FEATURE_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"DEAD_SEA_REQUIRES_ADJACENT_UNIT",
		"FeatureType",
		"FEATURE_DEAD_SEA"
	);
	```
