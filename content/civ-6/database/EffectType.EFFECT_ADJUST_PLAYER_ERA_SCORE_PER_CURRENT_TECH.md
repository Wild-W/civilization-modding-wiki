---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_CURRENT_TECH
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_CURRENT_TECH
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples

```SQL {title="DRAMATIC_AGES_ERA_SCORE_PER_CURRENT_TECH_COMPLETIONS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DRAMATIC_AGES_ERA_SCORE_PER_CURRENT_TECH_COMPLETIONS",
		"MODIFIER_ALL_PLAYERS_ADJUST_ERA_SCORE_PER_CURRENT_TECH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DRAMATIC_AGES_ERA_SCORE_PER_CURRENT_TECH_COMPLETIONS",
		"Amount",
		1
	);
	
```

