---
tags:
- RequirementType
title: REQUIREMENT_PLOT_WONDER_IS_ERA
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_WONDER_IS_ERA
>
> * Class: `Unknown`
> * Arguments:
>	* LatestEra `Unknown`
>	* EarliestEra `Unknown`

## Samples

```SQL {title="REQUIRE_THIS_WONDER_IS_ANCIENT_OR_CLASSICAL"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRE_THIS_WONDER_IS_ANCIENT_OR_CLASSICAL",
		"REQUIREMENT_PLOT_WONDER_IS_ERA"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRE_THIS_WONDER_IS_ANCIENT_OR_CLASSICAL",
		"EarliestEra",
		"ERA_ANCIENT"
	),
	(
		"REQUIRE_THIS_WONDER_IS_ANCIENT_OR_CLASSICAL",
		"LatestEra",
		"ERA_CLASSICAL"
	);
	```
