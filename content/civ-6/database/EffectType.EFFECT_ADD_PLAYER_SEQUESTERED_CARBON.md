---
tags:
- EffectType
title: EFFECT_ADD_PLAYER_SEQUESTERED_CARBON
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_PLAYER_SEQUESTERED_CARBON
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="PROJECT_COMPLETION_CARBON_SEQUESTRATION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"PROJECT_COMPLETION_CARBON_SEQUESTRATION",
		"MODIFIER_PLAYER_ADD_SEQUESTERED_CARBON"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PROJECT_COMPLETION_CARBON_SEQUESTRATION",
		"Amount",
		50000
	);
	
```

