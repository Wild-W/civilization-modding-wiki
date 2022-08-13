---
tags:
- RequirementType
title: REQUIREMENT_PLOT_IS_APPEAL_BETWEEN
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_IS_APPEAL_BETWEEN
>
> * Class: `PLOTS`
> * Arguments:
>	* MinimumAppeal `Integer`

## Samples

```SQL {title="REQUIRES_PLOT_BREATHTAKING_APPEAL"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLOT_BREATHTAKING_APPEAL",
		"REQUIREMENT_PLOT_IS_APPEAL_BETWEEN"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLOT_BREATHTAKING_APPEAL",
		"MinimumAppeal",
		4
	);
	
```
